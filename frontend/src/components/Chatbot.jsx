import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
    const [userInput, setUserInput] = useState('');
    const [chatHistory, setChatHistory] = useState([]);

    const sendMessage = async () => {
        try {
            const response = await axios.post('/api/chat/', { user_input: userInput });
            const botResponse = response.data.bot_response;
            setChatHistory([...chatHistory, { user: userInput, bot: botResponse }]);
            setUserInput('');
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    return (
        <div>
            <h1>Chatbot Interface</h1>
            <div>
                {chatHistory.map((message, index) => (
                    <div key={index}>
                        <p>User: {message.user}</p>
                        <p>Bot: {message.bot}</p>
                    </div>
                ))}
            </div>
            <input type="text" value={userInput} onChange={(e) => setUserInput(e.target.value)} placeholder="Type your message..." />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default Chatbot;