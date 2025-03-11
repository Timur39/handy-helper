const Chat = () => {
  var ws = new WebSocket("ws://localhost:8000/ws");
  ws.onmessage = function(event) {
      var messages = document.getElementById('messages')
      var message = document.createElement('li')
      var content = document.createTextNode(event.data)
      message.appendChild(content)
      messages.appendChild(message)
  };
  function sendMessage(event) {
      var input = document.getElementById("messageText")
      ws.send(input.value)
      input.value = ''
      event.preventDefault()
  }
  
  return <div>
    <h1>WebSocket Chat</h1>
    <form action="" onSubmit={sendMessage}>
        <input type="text" id="messageText" autoComplete="off"/>
        <button>Send</button>
    </form>
    <ul id='messages'>
    </ul>
  </div>

  };
  
export default Chat;