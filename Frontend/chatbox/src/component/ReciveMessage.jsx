import React, { useEffect, useState } from 'react'
import { Box,HStack, Image, Spinner, Text } from '@chakra-ui/react';
const logo = "assets/ai_logo.png";
const ReciveMessage = ({ message }) => {
    const [loadMess,setLoadMess]=useState('');
    useEffect(() => {
        const interval = setInterval(() => {
          setLoadMess(message)
        }, 400);   
        return () => clearInterval(interval);
      }, []);
    return (
        <>
            <Box position={"relative"} py={10} >
                <Image src={logo} height="50px" borderRadius={"full"} userSelect="none" />
                <Box background={"blackAlpha.300"} maxWidth="container.sm" position="absolute" top={"0"} left="10%" borderRadius={"12px"}>
                    <Box px={10} py={6} >
                        {!loadMess? <>
                            <HStack>
                                <Spinner color='red.500' />
                                <Text>Loading ...</Text>
                            </HStack>

                        </> : <Text>
                            {loadMess}
                        </Text>}
                    </Box>
                </Box>
            </Box>
        </>
    )
}

export default ReciveMessage