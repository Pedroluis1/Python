import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Carregar o modelo treinado para reconhecimento de caracteres
model = load_model('poker_model.h5')

# Dicionário que associa os valores das mãos de poker aos seus respectivos rótulos
poker_hands = {
    0: 'Carta Alta',
    1: 'Par',
    2: 'Dois Pares',
    3: 'Trinca',
    4: 'Straight',
    5: 'Flush',
    6: 'Full House',
    7: 'Quadra',
    8: 'Straight Flush',
    9: 'Royal Flush'
}

# Função que realiza o reconhecimento de caracteres em uma imagem de carta de poker
def recognize_cards(image):
    # Definir as regiões de interesse na imagem (uma para cada carta)
    card1 = image[0:100, 0:70]
    card2 = image[0:100, 70:140]

    # Redimensionar as regiões de interesse para o tamanho esperado pelo modelo
    card1 = cv2.resize(card1, (30, 40))
    card2 = cv2.resize(card2, (30, 40))

    # Converter as imagens para escala de cinza e normalizar os pixels
    card1 = cv2.cvtColor(card1, cv2.COLOR_BGR2GRAY) / 255.0
    card2 = cv2.cvtColor(card2, cv2.COLOR_BGR2GRAY) / 255.0

    # Adicionar uma dimensão extra às imagens para serem compatíveis com a entrada do modelo
    card1 = np.expand_dims(card1, axis=-1)
    card2 = np.expand_dims(card2, axis=-1)

    # Realizar a inferência do modelo nas duas imagens
    prediction1 = model.predict(np.array([card1]))[0]
    prediction2 = model.predict(np.array([card2]))[0]

    # Converter as predições em valores numéricos de cartas (2 a 14)
    card1_value = np.argmax(prediction1) + 2
    card2_value = np.argmax(prediction2) + 2

    # Converter as predições em naipes (C, D, H, S)
    card1_suit = np.argmax(prediction1[4:])  # As primeiras quatro classes são os valores das cartas
    card2_suit = np.argmax(prediction2[4:])

    # Retornar os valores das duas cartas
    return [(card1_value, card1_suit), (card2_value, card2_suit)]

# Função que determina o valor da mão de poker a partir das cartas reconhecidas
def determine_poker_hand(cards):
    # Separar os valores das cartas e dos naipes em duas listas distintas
    card_values = [card[0] for card in cards]
    card_suits = [card[1] for card in cards]

    # Verificar se todas as cartas têm o mesmo naipe (flush)
    flush = len(set(card_suits)) == 1

    # Verificar se as cartas formam uma sequência (straight)
    straight = False
    if len(set(card_values)) == 5 and max(card_values) - min(card_values) == 4:
        straight = True

    # Verificar se há cartas com o mesmo valor (pares, trincas, etc)
    pairs = []
    triples = []
    quads = []
    for value in set(card_values):
        count = card_values.count(value)
        if count == 2:
            pairs.append(value)
        elif count == 3:
            triples.append(value)
        elif count == 4:
            quads.append(value)

    # Determinar o valor da mão de acordo com as combinações de cartas
    if flush and straight and max(card_values) == 14:
        return poker_hands[9]  # Royal Flush
    elif flush and straight:
        return poker_hands[8]  # Straight Flush
    elif quads:
        return poker_hands[7]  # Quadra
    elif triples and pairs:
        return poker_hands[6]  # Full House
    elif flush:
        return poker_hands[5]  # Flush
    elif straight:
        return poker_hands[4]  # Straight
    elif triples:
        return poker_hands[3]  # Trinca
    elif len(pairs) == 2:
        return poker_hands[2]  # Dois Pares
    elif pairs:
        return poker_hands[1]  # Par
    else:
        return poker_hands[0]  # Carta Alta

    # Detect the contours of the cards
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour of the hand with the largest area
    max_area = 0
    best_cnt = None
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt

    # If no hand was found, return None
    if best_cnt is None:
        return None

    # Create a mask for the hand contour
    mask = np.zeros_like(thresh)
    cv2.drawContours(mask, [best_cnt], 0, 255, -1)

    # Apply the mask to the image
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    # Crop the image to the bounding box of the hand contour
    x, y, w, h = cv2.boundingRect(best_cnt)
    cropped_img = masked_img[y:y + h, x:x + w]

    # Resize the cropped image to a fixed size
    cropped_img = cv2.resize(cropped_img, (800, 800))

    # Apply a bilateral filter to smooth the image
    blurred_img = cv2.bilateralFilter(cropped_img, 9, 75, 75)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding to binarize the image
    _, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find the contours of the cards in the hand
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Sort the contours from left to right
    cnts = sorted(cnts, key=lambda c: cv2.boundingRect(c)[0])

    # Define the values for each card rank
    ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    # Define the values for each card suit
    suits = {'S': 4, 'H': 3, 'D': 2, 'C': 1}

    # Initialize the list of cards and the list of ranks
    cards = []
    card_ranks = []

    # Loop over the contours of the cards
    for cnt in cnts:
        # Crop the card from the image
        x, y, w, h = cv2.boundingRect(cnt)
        card_img = gray_img[y:y + h, x:x + w]

        # Find the largest contour in the card
        _, cnts, _ = cv2.findContours(card_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=lambda c: cv2.contourArea(c), reverse=True)
        largest_cnt = cnts[0]

        # Create a mask for the largest contour
        mask = np.zeros_like(card_img)
        cv2.drawContours(mask, [largest_cnt], 0, 255, -1)

        # Apply the
def identify_strongest_hand(hand1, hand2):
    """
    Identifica qual das duas mãos é a mais forte.

    :param hand1: mão 1 do jogo de poker (representada por uma lista de 5 cartas)
    :param hand2: mão 2 do jogo de poker (representada por uma lista de 5 cartas)
    :return: a string com a descrição da mão mais forte (Exemplo: "Royal flush")
    """

    # Verifica a força da mão 1
    hand1_strength = get_hand_strength(hand1)

    # Verifica a força da mão 2
    hand2_strength = get_hand_strength(hand2)

    # Compara as forças das mãos e retorna a mais forte
    if hand1_strength > hand2_strength:
        return hand_strength_to_string(hand1_strength)
    elif hand2_strength > hand1_strength:
        return hand_strength_to_string(hand2_strength)
    else:
        return "Empate"
# Carrega a imagem
image = cv2.imread('poker.jpg')

# Identifica as duas mãos
hand1, hand2 = detect_hands(image)

# Identifica a mão mais forte
strongest_hand = identify_strongest_hand(hand1, hand2)

# Exibe o resultado
print("Mão mais forte:", strongest_hand)
