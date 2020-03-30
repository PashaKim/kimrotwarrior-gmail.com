
def dict_reformat(orig_d):
    '''
    :param orig_d: dict
    :return: reformat_d: dict
    '''
    reformat_d = dict()

    def cell(parent, child, value):
        return {parent: {child: value}}

    for orig_key, orig_value in orig_d.items():
        row_dict = dict()
        if ':' in orig_key:
            keys = orig_key.split(':')
            for index, key in enumerate(keys):
                try:
                    row_dict.update(cell(keys[index], keys[index+1], orig_value))
                except IndexError:
                    continue
            else:
                for key, value in row_dict.items():
                    try:
                        reformat_d[key].update(value)
                    except KeyError:
                        reformat_d[key] = value
    return reformat_d


def dict_delta(dict_1, dict_2):
    '''
    :param dict_1: dict
    :param dict_2: dict
    :return: delta_d: dict
    '''
    delta_d = dict()
    for key, value in dict_1.items():
        if key in dict_2:
            try:
                delta_d[key] = int(dict_1[key]) - (dict_2[key])
            except TypeError:
                pass
    return delta_d