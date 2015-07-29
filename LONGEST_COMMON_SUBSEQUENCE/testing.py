set_cd = {'Q', 'p', 'U', 'I', 'j', 'N', 'J', 's', 'x', 'w', 'O', 'M', 'H',
          'n', 'a', 'V', 'v', 'd', 'e', 'W', 'f'}

aa = 'XMJAUZ'
bb = 'MZJAXU'

cc = 'spndvOOWIJfnaQVNNaUxwHIsdfxMjveI'
dd = 'QJHwOvseVMWHxafHpxUUVnMsVIdNUwjes'

ee = 'ABC'
ff = 'FBC'

cc_char_dict = {}
dd_char_dict = {}

for char in dd:
    cc_char_dict[char] = cc.index(char)

for char in cc:
    dd_char_dict[char] = dd.index(char)


print(cc_char_dict)
print(dd_char_dict)

loc_diff = {}

for char in cc:
    loc_diff[char] = abs(cc_char_dict[char] - dd_char_dict[char])