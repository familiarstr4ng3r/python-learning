import googletrans
import win32ui
import win32con

# ! https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group/52456197

# ! 3.1.0-alpha
translator = googletrans.Translator()

#print(googletrans.__version__)

# ! en english
# ! ru russian
# ! uk ukrainian

result = translator.translate("Hello, World!", dest="ru")

print(result.text)

code = win32ui.MessageBox(result.text, "Title", win32con.MB_YESNO) 

if code == win32con.IDYES:
  print("YES")
elif code == win32con.IDNO:
  print("NO")