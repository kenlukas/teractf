# Information

## Forensics

### Files can always be changed in a secret way. Can you find the flag

This challenge came with an image file, which immediately makes me thing Steganography.

![cat.jpg](./cat.jpg)

Step one, look at the image.  The code in the background caught my attention.  But that seems a little complicated for an easy challenge.
Step two, exiftools

```sh
exiftool cat.jpg
ExifTool Version Number         : 13.30
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2021:03:15 14:24:46-04:00
# Information
File Access Date/Time           : 2025:05:30 10:52:38-04:00
File Inode Change Date/Time     : 2025:05:30 10:52:36-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```
The Current IPTC Digest and License fields caught my attention.  The former looked like it could be some type of encoding.  The latter definitely looked like base64 encoding.  

```sh
% echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" |base64 -d
picoCTF{the_m3tadata_1s_modified}
```

**picoCTF{the_m3tadata_1s_modified}**
