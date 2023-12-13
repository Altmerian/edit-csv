import codecs
import json

hex_encoded_string = r"{\x22area\x22:\x22Production\x22,\x22pre-filter\x22:\x22((sapVendorStatus = \x5C\x22APPROVED - ALL BUSINESS\x5C\x22 OR sapVendorStatus = \x5C\x22APPROVED - CONDITIONS APPLY\x5C\x22) AND quickOrderProduct != \x5C\x22Yes\x5C\x22 AND approvalStatus = \x5C\x22approved\x5C\x22 AND gbi_restrictionCode = \x5C\x22false\x5C\x22 AND gbi_sapDealerCode = \x5C\x22false\x5C\x22 AND sapDeletionFlag != \x5C\x22Yes\x5C\x22)\x22,\x22clientKey\x22:\x222a676d20-ea81-476f-a809-8c08d882ca1a\x22,\x22biasing\x22:{\x22augmentBiases\x22:\x22true\x22,\x22biases\x22:[{\x22strength\x22:\x22Strong_Increase\x22,\x22name\x22:\x22gbi_inStock\x22,\x22content\x22:\x22CHIL\x22},{\x22strength\x22:\x22Medium_Increase\x22,\x22name\x22:\x22gbi_inStock\x22,\x22content\x22:\x22ZJIL\x22},{\x22strength\x22:\x22Medium_Increase\x22,\x22name\x22:\x22gbi_inStock\x22,\x22content\x22:\x22ZSMO\x22}]},\x22pageSize\x22:\x2250\x22,\x22pruneRefinements\x22:false,\x22skip\x22:\x2226500\x22,\x22collection\x22:\x22GraybarProd\x22,\x22fields\x22:[\x22*\x22],\x22refinements\x22:[{\x22navigationName\x22:\x22gbi_categories.1\x22,\x22value\x22:\x22Conduit, Raceway and Cable Support\x22}]}"

decoded_string = codecs.decode(hex_encoded_string.encode(), 'unicode_escape')

decoded_json = json.loads(decoded_string)

print(json.dumps(decoded_json, indent=4, sort_keys=True))

# print(decoded_string)
