import { Box, Button, Flex, HStack, Input } from "@chakra-ui/react"
import { useState } from "react";
import axios from 'axios'
import ReciveMessage from "./component/ReciveMessage";
import SendMessage from "./component/SendMessage";
import { useEffect } from "react";


function App() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([{}]);
  useEffect(() => {
    var elem = document.getElementById('chatLayout');
    elem.scrollTop = elem.scrollHeight;
  }, [chat.length])


  const handleSubmit = () => {
    if (message !== '') {
      axios.post('http://127.0.0.1:5000/user', { 'message': message })
        .then(res => {
          let ch = chat;
          ch.push({ from: "our", message: message })
          ch.push({ from: "ai", message: res.data })
          setChat(ch);
          setMessage('');


        })
        .catch(err => {
          console.log(err);
        });
    }

  }
  return (
    <Box background={"rgba(245, 228, 228, 1)"} height="100vh">
      <Flex pt={16} alignItems={"center"} justifyContent="center" width={"full"}>
        <Box borderRadius={"12px"} background="gray.500" width="container.md" height={"container.md"}>
          <Flex id="chatLayout" flexDirection={
            'column'
          } gap={6} px={8} py={14} height={"700px"} overflowY="auto" overscrollBehaviorY={"contain"} scrollBehavior="smooth">

            <ReciveMessage message={"Welcome Back"} />
            {chat.map((item, index) => {
              return item.from === "ai" ? <ReciveMessage key={index} message={item.message} /> : <SendMessage key={index} message={item.message} />
            }
            )}

          </Flex>
          <Box background={"white"} position="sticky" bottom={"0%"} zIndex={"99"}>
            <HStack alignItems={"center"} gap={4} py={8} px={6} >
              <Input placeholder='Send ...........' value={message} onChange={(e) => setMessage(e.target.value)} />
              <Button px={6} py={4} colorScheme={"blue"} onClick={handleSubmit}>
                Send
              </Button>
            </HStack>
          </Box>
        </Box>

      </Flex>
    </Box>
  );
}

export default App;
