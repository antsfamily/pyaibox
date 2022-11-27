
import pyaibox as pb

path = 'data/files/english_sentence.txt'

h = pb.HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)
