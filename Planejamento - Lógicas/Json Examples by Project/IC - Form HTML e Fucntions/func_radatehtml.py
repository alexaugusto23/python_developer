def _fn(period, rotate = False):
    if rotate:
        _format = f"""
        <html>
        <head>
        <style>
        
        #rotate-text {{
            height : 70px;
            display : flex;
            align-items : center;
            justify-content : center;
            transform: rotate(90deg);
        }}
        
        </style>
        </head>
        <body>
        
        <div id="rotate-text">
          <p><b>{period}</b></p>
        </div>
        
        </body>
        </html>
        """
    else:
        _format = f"""
        <html>
        <head>
        <style>
        
        #allign-text {{
         height : 70px;
         display : flex;
         align-items : center;
         justify-content : center;
        }}
        
        </style>
        </head>
        <body>
        
        <div id="allign-text">
          <p><b>{period}</b></p>
        </div>
        
        </body>
        </html>
        """
        
    return _format

result = _fn