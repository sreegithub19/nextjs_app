from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_self(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str('''
<!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1"> <style> body, html { height: 100%; margin: 0; } .content { position: absolute; top: 15%; left:25%; background: rgb(0, 0, 0); /* Fallback color */ background: rgba(0, 0, 0, 0.76); /* Black background with 0.5 opacity */ color: #f1f1f1; width: 50%; padding: 20px; } .bg { /* The image used */ background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcRqNquWxQHJAPgugDwzXokAU_dQUXzknUTA&usqp=CAU"); /* Full height */ height: 100%; /* Center and scale the image nicely */ background-position: center; background-repeat: no-repeat; background-size: cover; } table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } div.parent { text-align: center; } ul { display: inline-block; text-align: left; }</style>
    </head> <body> <div class="bg"></div>  <div class="content"> <h1 id="home" 
        style="text-align: center;font-weight: bold;text-decoration: underline;">
            WELCOME TO JAVASCRIPT APPLICATIONS!!</h1> 
   <h3 style="text-align:center;"> Click on any of the below JavaScript apps!</h3>
   <div class="parent"> <ul>
        <li><a href='/api/calculator'>Calculator</a></li> 
       <li><a href='/api/maze'>Maze</a></li>
        <li><a href='/api/tic_tac_toe'>Tic-tac-toe</a></li>
        <li><a href='/api/clock'>Analogue clock</a></li>
        <li><a href='/api/hangman'>Hangman</a></li>
        <li><a href='/api/puzzles'>Puzzles</a></li>
        <li><a href='/api/sudoku'>Sudoku</a></li>
        <li><a href='/api/virtual_keyboard'>Virtual keyboard</a></li>
	<li><a href='/api/solitaire'>Solitaire</a></li>
	<li><a href='/api/chess'>Chess</a></li>
	<li><a href='/api/dino'>Dino</a></li>
	<li><a href='/api/sass_'>Sass</a></li>
	<li><a href='/api/tilt_maze'>Tilted Maze</a></li>
	<li><a href='/api/codepen'>Codepen</a></li>
   </ul> </div> 
       </div> </body> </html>
    ''').encode())
        return
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str('''
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Virtual Keyboard ⌨️ </title>
        <style>
            body * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: Arial, Helvetica, sans-serif;
    }
    
    
    .keyboard-base{
        max-width: 1085px;
        padding: 20px;
        position: absolute;
        top: 30%;
        background-color: rgb(252, 185, 185);
        border-radius: 10px;
        justify-content: center;
    
    
    }
    .section-a{
        display: flex;
    }
    
    .key {
        background-color: rgb(243, 243, 243);
        border: 2px solid black;
        border-radius: 5px;
        
        font-size: 20px;
        text-align: center;
        padding-top: 17px;
        width:50px;
        height:50px;
        margin:5px;
    }
    
    .key:hover{
        background-color: rgb(247, 100, 161);
    }
    .space {
        width: 100%;
    }
    
    .capslock{
        width:30%;
    }
    .leftshift{
        width:20%;
    }
    .return {
        width:20%;
        
    }
    textarea{
        width: 30%;
        height: 70px;
        font-size: 30px;
    }
        </style>
    </head>
    <body>
        <textarea type="text" id="inputText" value="" autofocus onblur="this.focus()" onkeydown="return false" onmouseup="getCaretPositon()"></textarea>
        
        <div class="keyboard-base">
        <div class="section-a">
            <div class="key" onclick="keyboardHandler(event)">~</div>
            <div class="key" onclick="keyboardHandler(event)">1</div>
            <div class="key" onclick="keyboardHandler(event)">2</div>
            <div class="key" onclick="keyboardHandler(event)">3</div>
            <div class="key" onclick="keyboardHandler(event)">4</div>
            <div class="key" onclick="keyboardHandler(event)">5</div>
            <div class="key" onclick="keyboardHandler(event)">6</div>
            <div class="key" onclick="keyboardHandler(event)">7</div>
            <div class="key" onclick="keyboardHandler(event)">8</div>
            <div class="key" onclick="keyboardHandler(event)">9</div>
            <div class="key" onclick="keyboardHandler(event)">0</div>
            <div class="key" onclick="keyboardHandler(event)">-</div>
            <div class="key" onclick="keyboardHandler(event)">+</div>
        </div>
        <div class="section-a">
            <div class="key" onclick="keyboardHandler(event)">Q</div>
            <div class="key" onclick="keyboardHandler(event)">W</div>
            <div class="key" onclick="keyboardHandler(event)">E</div>
            <div class="key" onclick="keyboardHandler(event)">R</div>
            <div class="key" onclick="keyboardHandler(event)">T</div>
            <div class="key" onclick="keyboardHandler(event)">Y</div>
            <div class="key" onclick="keyboardHandler(event)">U</div>
            <div class="key" onclick="keyboardHandler(event)">I</div>
            <div class="key" onclick="keyboardHandler(event)">O</div>
            <div class="key" onclick="keyboardHandler(event)">P</div>
            <div class="key" onclick="keyboardHandler(event)">[</div>
            <div class="key" onclick="keyboardHandler(event)">]</div>
            <div class="key backslash" onclick="keyboardHandler(event)">\</div>
        </div>
        <div class="section-a">
    
            <div class="key capslock" onclick="keyboardHandler(event)">CapsLock</div>
            <div class="key" onclick="keyboardHandler(event)">A</div>
            <div class="key" onclick="keyboardHandler(event)">S</div>
            <div class="key" onclick="keyboardHandler(event)">D</div>
            <div class="key"onclick="keyboardHandler(event)">F</div>
            <div class="key"onclick="keyboardHandler(event)">G</div>
            <div class="key"onclick="keyboardHandler(event)">H</div>
            <div class="key"onclick="keyboardHandler(event)">J</div>
            <div class="key" onclick="keyboardHandler(event)">K</div>
            <div class="key" onclick="keyboardHandler(event)">L</div>
            <div class="key" onclick="keyboardHandler(event)">;</div>
            <div class="key" onclick="keyboardHandler(event)">'</div>
            <div class="key return" onclick="keyboardHandler(event)">Back</div>
        </div>
        <div class="section-a">
    
            <div class="key leftshift" onclick="keyboardHandler(event)">Shift</div>
            <div class="key" onclick="keyboardHandler(event)">Z</div>
            <div class="key" onclick="keyboardHandler(event)">X</div>
            <div class="key" onclick="keyboardHandler(event)">C</div>
            <div class="key" onclick="keyboardHandler(event)">V</div>
            <div class="key" onclick="keyboardHandler(event)">B</div>
            <div class="key" onclick="keyboardHandler(event)">N</div>
            <div class="key" onclick="keyboardHandler(event)">M</div>
            <div class="key" onclick="keyboardHandler(event)">,</div>
            <div class="key" onclick="keyboardHandler(event)">.</div>
            <div class="key" onclick="keyboardHandler(event)">/</div>
        </div>
        <div class="section-a">
            <div class="key space" onclick="keyboardHandler(event)">Space</div>
            </div>
        </div>
    </body>
    <script>
        var input = document.getElementById("inputText");
    let bool = false;
    
    const keyboardHandler = (event) => {
      const caretPositon = getCaretPositon();
      const targetValue = event.target.innerText;
      let array = input.value.split("");
      let a;
    
      switch (targetValue) {
        case "Back":
          console.log(caretPositon);
          if (caretPositon == 0) {
            input.setSelectionRange(0, 0);
          } else {
            array.splice(caretPositon - 1, 1);
            a = array.join("");
            input.value = a;
            input.setSelectionRange(caretPositon - 1, caretPositon - 1);
          }
    
          break;
        case "CapsLock":
          toggleCaps();
          break;
        case "Shift":
          toggleShift();
          break;
        case "Space":
          array.splice(caretPositon, 0, " ");
          a = array.join("");
          input.value = a;
          input.setSelectionRange(caretPositon + 1, caretPositon + 1);
    
          break;
        default:
          array.splice(caretPositon, 0, event.target.innerText);
          a = array.join("");
          input.value = a;
          input.setSelectionRange(caretPositon + 1, caretPositon + 1);
    
          if (bool) {
            bool = false;
            toggleCaps();
          }
      }
    };
    
    function getCaretPositon() {
      return input.selectionStart;
    }
    
    const isUpperCase = (string) => /^[A-Z]*$/.test(string);
    
    const toggleCaps = () => {
      let keyboardKeys = document.getElementsByTagName("div");
      for (let i = 13; i < keyboardKeys.length; i++) {
        const innerElText = keyboardKeys[i].innerText;
        const innerTextLength = innerElText.length;
    
        if (innerTextLength == 1 && isUpperCase(innerElText)) {
          keyboardKeys[i].innerText = innerElText.toLowerCase();
        } else if (innerTextLength == 1) {
          keyboardKeys[i].innerText = keyboardKeys[i].innerText.toUpperCase();
        }
      }
    };
    
    const toggleShift = () => {
      toggleCaps();
      bool = true;
    };
    
    </script>
    </html>
    '''
    
    ).encode())
        return

    def do_GET(self):
        self.do_self()