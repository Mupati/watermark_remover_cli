## watermark_remover_cli

A simple package for removing watermarks from PDFs and images.

I built a web application as well. This is the link: [Watermark Remover Web App](https://watermark-remover.herokuapp.com)

## Installation
- Install using pip <br/>
  ```pip install watermark-remover-cli```

- Usage <br/>
  ```python3 -m watermark-remover-cli --file "path/to/pdf/file```
  
## TODO
It currently works for PDFs with colored watermarks and black text for the main content
- [ ] Handle image input
- [ ] Making it generic for colored text
- [ ] Removing watermarks with drop-shadows
- [ ] Determining color of text with color histograms with KNN Alogrithm or another technique


## Done ✓
- [x] Handle PDF input