def clean(text):
    result = ""
    notAppend = False

    for i in list(text):
        if i =="[":
            notAppend = True
        if notAppend:
            pass
        else:
            result +=i
        if i =="]":
            notAppend = False

    return result

print(clean("[adsasdasd]tttttttt[asdas]"))