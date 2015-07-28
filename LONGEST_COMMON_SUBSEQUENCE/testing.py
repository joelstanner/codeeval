set_cd = {'Q', 'p', 'U', 'I', 'j', 'N', 'J', 's', 'x', 'w', 'O', 'M', 'H', 'n', 'a', 'V', 'v', 'd', 'e', 'W', 'f'}

aa = 'XMJAUZ'
bb = 'MZJAXU'

cc = 'spndvOOWIJfnaQVNNaUxwHIsdfxMjveI'
dd = 'QJHwOvseVMWHxafHpxUUVnMsVIdNUwjes'

cc_char_dict = {}
dd_char_dict = {}

for char in dd:
    cc_char_dict[char] = cc.index(char)

for char in cc:
    dd_char_dict[char] = dd.index(char)


print(cc_char_dict)
print(dd_char_dict)
