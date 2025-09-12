""" programming_lang_stat = dict ()
programming_lang_input = input().strip().split(',')
programming_lang_display_index = list()

for programming_lang_key in programming_lang_input:
    if programming_lang_key not in programming_lang_stat:
        programming_lang_stat[programming_lang_key] = 1
        programming_lang_display_index.append(programming_lang_key)
    else:
        programming_lang_stat[programming_lang_key] += 1

for i in range (len(programming_lang_display_index)):
    print(programming_lang_display_index[i], programming_lang_stat[programming_lang_display_index[i]]) """


satatics = dict()
lang_input = input().strip().split(',')
#' A ' => 'A'
#'JavaScript,TypeScript,JavaScript,React,Vue,JavaScript' => 
# ['JavaScript', 'TypeScript', 'JavaScript', 'React', 'Vue', 'JavaScript']

for key in lang_input:
    if key not in satatics:
        satatics[key] = 1
    else:
        satatics[key] += 1

display_index = list(satatics.keys())

for i in range(len(display_index)):
    print(display_index[i], satatics[display_index[i]])