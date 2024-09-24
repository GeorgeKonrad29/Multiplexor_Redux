import re
from string import ascii_uppercase



def check_weights(weights):
    # Modificamos la regex para permitir varios números separados por comas
    match = re.match(r"^\s*(?:\d+\s*,?\s*)+$", weights)
    if match:
        l = to_list(match.string)
        if int(l[-1]) <= 1:  # Si el último número es <= 1, consideramos inválido
            return False
        return True
    return False





def quant_vars(weights):
    # Verificamos que pesos no esté vacío
    if not weights:
        return 0  # O maneja el caso según sea necesario
    last_weight = int(weights[-1])  # Convertimos el último peso a entero
    quantity_vars = len(bin(last_weight)) - 2  # Calculamos la cantidad de variables
    return quantity_vars




def process_vars(weights: str, quant=None):
    match = check_weights(weights)
    if not match:
        return None, None
    weights = to_list(weights)
    weights.sort(key=int)
    if not quant:
        quanti_vars = quant_vars(weights)
    else:
        quanti_vars = int(quant)
    
    if quanti_vars <= 0:  # Asegurarse de que las variables sean válidas
        return None, None
    
    vars = list(ascii_uppercase[:quanti_vars])
    return vars, quanti_vars


def to_list(str_: str):
    # Elimina espacios y divide la cadena por comas
    items = str_.strip().split(",")
    # Filtra elementos vacíos y devuelve la lista
    return [item.strip() for item in items if item.strip()]




def convert_number_binary(mntrms):
    mx_mntrm = max(mntrms) if mntrms else 0
    n_bts = mx_mntrm.bit_length() if mx_mntrm > 0 else 1
    b_dic = {}
    for i in range(2 ** n_bts):
        b_l = [int(bt) for bt in format(i, f'0{n_bts}b')]
        b_dic[i] = b_l
    return b_dic



def grouping(binary_data):
    grp = {
        'A´': [], 
        'A': []  
    }
    
    for password, binary_list in binary_data.items():
        # Validar que la lista contiene solo valores binarios
        if not all(bit in [0, 1] for bit in binary_list):
            raise ValueError("Cada lista debe contener solo valores binarios (0 o 1).")
        
        decimal = int("".join(map(str, binary_list)), 2)
        
        # Clasificar basado en el primer bit
        if binary_list[0] == 0: 
            grp['A´'].append(decimal)
        else:  
            grp['A'].append(decimal)

    return grp




def reduct(minterms: list, variables: list) -> list:
    """
    Reduce una lista de términos mínimos basándose en las variables proporcionadas.

    Args:
        minterms (list): Lista de términos mínimos.
        variables (list): Lista de variables utilizadas en la función.

    Returns:
        list: Lista reducida de términos.
    """
    if not variables:
        raise ValueError("La lista de variables no puede estar vacía.")

    quant_mn_trms = 2 ** len(variables)
    result = []
    principal_variable = variables[0]
    length = quant_mn_trms // 2

    for i, j in zip(range(length), range(length, quant_mn_trms)):
        if i in minterms and j in minterms:
            result.append(1)
        elif i in minterms:
            result.append(f"{principal_variable}'")
        elif j in minterms:
            result.append(principal_variable)
        else:
            result.append(0)
    
    return result

def convert_vector(strg_numbers: str) -> list:
    """
    Convierte una cadena de números separados por comas en una lista de enteros.

    Args:
        strg_numbers (str): Cadena de números separados por comas.

    Returns:
        list: Lista de enteros convertidos.
    """
    try:
        vector = [int(n.strip()) for n in strg_numbers.split(",")]
    except ValueError:
        raise ValueError("Todos los elementos deben ser números enteros válidos.")
    
    return vector

