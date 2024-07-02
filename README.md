Dictionary Method Used in PDFSHORT project has been reused in Image Compression and Has Not shown any improvement Yet. But The ideas are growing and I am going with the Flow.
I have used 1byte to fit in 2 pixels. Which has been a huge progress for space utilization (SAD) and still the image compression data is double the size of original image.

Still In Initial State (Worst Version 1.0) (Basic Layout of DCT and Dictionary Method)

Inital Commit Joke:
The Image size has been doubled after the method applied and still will be increased because i have not mentioned blocks dictionary(sad in blue)

Its Not a Guaranteed method But is Best For Space Pictures like MilkyWay Galaxy which has minimum number of colours compared to earth photography.
I think when the space telescopes sends data form outer space it needs to send minimum information of the image captured faster in bits forms rather than any other format.
This method doesn't Guarantee for Earth normally but might be useful for outer space photography😂LOL
But Still it is an assumption as I haven't tested it yet but the fresh idea in my mind says so And Sorry to say I have been wrong Many times before. Don't Trust Me.

Again the representation of data in our hard disk is the major problem for us as we can utilize the unset bits which doesnt represent any data.
For now I think a finetuning can help in the case where we check each row and column and delete the rows or column which has no setbits and mark it with a single bit saving atleast O(height) or O(width) bit space
for further we can also take a range where there are unset bits and delete the ranged rows or column and mark with a 1byte space and 1bit information but there are many complications thats why we need a intelligent self working patterns for the image compression which backtracks if the size is not decreased.
*For frequently used pictures this method may not be quite useful but for image which needs to be stored and not used for long time needs kind of compression format like this which stores only useful bits and compresses the bits more further
but to be practicle frequently used pictures needs more attention for compression and if the method idea grows further we can see so development in the program.

Future Updates:
But I am working with (ANA🌻) aka A.NEGATION.ANALYSIS Method to further minimize the size. The idea is just an assumption or imagination and works in my mind but cant be practical right now as the idea doesn't grow if i am practical. I am implementing it and it has multiple layers and works on blocks intelligently so it needs a proper hard coding before progressing with a fully functional intelligent prototype. 
Hope it Might Work 

Takling about compression we can also use a modification technique which matches the similarity of two pixels and if the similarities are very low we can change the pixels boundaries range optimally viable and also optically correct to a same rgb value to increase the DCT this will help us in compressing the image file and .bin file
because as of now we are considering all pixels and storing it but we can use DCT to make a block of specific height and width and store the single value for it we can combine DCT with A.N.A to create a better blocks for now

