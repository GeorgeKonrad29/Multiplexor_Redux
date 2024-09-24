import BACK.back as bc

if __name__ == "__main__":
    #ACA ES DONDE ENTRAN LOS DATOS
    values = "1,4,10,11,15,20"
    # Convertir cadena a lista de enteros antes de pasar a convertir_a_binario
    minterms = bc.convert_vector(values)
    b_l = bc.convert_number_binary(minterms)
    grouping = bc.grouping(b_l)
    print(grouping)
    vars, _ = bc.process_vars(values)
    print(vars)
    choice_vars = vars[1:]
    print(choice_vars)
    minterms.sort()
    result = bc.reduct(minterms, vars)
    #ACA ES DONDE SALE LA RESPUES FINAL
    final_result = result
    print(final_result)