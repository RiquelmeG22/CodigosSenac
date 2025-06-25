import React, { useState } from "react";
import { StyleSheet, Text, View, TouchableOpacity } from "react-native"; 


export default function NewWindow() {

    const [board, setBoard] = useState(Array().fill(null));
    const [isXturn, setIsXTurn] = useState(true);
    const [gameResult, setGameResult] = useState(null);
    const winnigCombinatios = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6],
    ];

    const handlePress = (index) => {
        if (board[index] || gameResult) return;

        const newBoard = [...board];
        newBoard[index] = isXturn ? 'X' : 'O';
        setBoard(newBoard);
        setIsXTurn(!isXturn);

        const winner = checkWinner(newBoard);
        if(winner){
            setGameResult(`${winner} Venceu`);
            return;
        }

        if(!newBoard.includes(null)){
            setGameResult('Empate');
        }
    };

    const checkWinner = (currentBoard) => {
        for(let combination of winnigCombinatios){
            const [a,b,c] = combination;
        if(currentBoard[a] && currentBoard[a] === currentBoard[b] && currentBoard[a] === currentBoard[c])
        return currentBoard[a];
        }
    }

    return null
};

const renderCell = (index) =>(
    <TouchableOpacity>
        style={styles.cell}
        onPress={}
    </TouchableOpacity>
)

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center' 
    },

    cell: {
        flex: 1,
        borderWidth: '#ccc',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#f9f9f9',
    }
});
