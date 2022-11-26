import { Box, Image, Text } from '@chakra-ui/react';
import React from 'react'

const logo = "https://img.hoidap247.com/picture/question/20210629/large_1624929680836.jpg";
const SendMessage = ({ message }) => {

    return (
        <>
            {!message ? <></> :
                <Box py={8}>
                    <Box position={"relative"}>
                        <>
                            <Box background={"blue.400"} maxWidth="container.sm" position="absolute" top={"0"} borderRadius={"12px"} right="10%">
                                <Box px={10} py={6}>
                                    <Text color={"white"}>
                                        {message}
                                    </Text>
                                </Box>
                            </Box>
                            <Image src={logo} height="50px" borderRadius={"full"} userSelect="none" float={"right"} />
                        </>
                    </Box>
                </Box>
            }
        </>

    )
}

export default SendMessage