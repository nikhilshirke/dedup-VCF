import re

unique_contacts = {}
input_file = r'C:\Users\nshirke\Downloads\AAA and 1338 others.vcf'
with open (input_file, encoding="utf8") as fh:
    data = fh.read()
    # print(data)
    contacts = re.compile(r"BEGIN:VCARD(.+?)END:VCARD", re.DOTALL)
    for match in contacts.finditer(data):
        # print(match)
        contact = match.groups()
        unique_contacts[str(f'BEGIN:VCARD{contact[0]}END:VCARD\n')] = 1

output_file = r'C:\Users\nshirke\Downloads\unique_contacts.vcf'
with open (output_file, 'w',encoding="utf8") as fh:
    for conntact in unique_contacts.keys():
        print(f'---------{conntact}')
        fh.write(conntact)