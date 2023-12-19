def pars_candidat_sj(candidat):
    candidat_format = candidat
    for del_symbol in ["<p>", "</p>", "<ul>", "</ul>", "<li>", "</li>", "<b>", "</b>", "<br />"]:
        candidat_format = candidat_format.replace(del_symbol, '')

    s = 'Обязанности'
    t = 'Требования'
    y = 'Условия'
    about = candidat_format
    requirements = candidat_format
    if s in candidat_format:
        if t in candidat_format:
            about = candidat_format[candidat_format.index(s):candidat_format.index(t)]
            if y in candidat_format:
                requirements = candidat_format[candidat_format.index(t):candidat_format.index(y)]
            else:
                requirements = candidat_format[candidat_format.index(t):]
        elif y in candidat_format:
            about = candidat_format[candidat_format.index(s):candidat_format.index(y)]

    return about, requirements