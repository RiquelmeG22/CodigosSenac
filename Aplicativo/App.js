import React, { useState } from 'react';
import AntDesign from '@expo/vector-icons/AntDesign';
import { StyleSheet, Text, View, Image, TouchableOpacity, TextInput } from 'react-native';

export default function App() {
 
  const [heartColor, setHeartColor] = useState('gray');
  const [senha, setSenha] = useState('');

  const [inputValue, setInputValue] = useState('');

  const toggleHeartColor = () => {
    setHeartColor(heartColor === 'red' ? 'gray' : 'red');
  };


  const showAlert = () => {
    try {
      alert(`Valor digitado: ${inputValue}`);
    } catch (error) {
      console.error("Erro no show alert: " + error);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.box}>

      <Image
        source={{ uri: 'https://github.com/riquelmeG22.png' }}
        style={styles.image} />
      
      <Text>Riquelme</Text>

      <TextInput
        style={styles.input}
        placeholder="Login .."
        value={inputValue} 
        onChangeText={(text) => setInputValue(text)} 
      />

      <TextInput 
        style={styles.input}
        placeholder="Senha .."
        value={senha} 
        onChangeText={(text) => setSenha(text)} 
        secureTextEntry={true}
      />

    
      <TouchableOpacity onPress={toggleHeartColor}>
        <AntDesign name="heart" size={24} color={heartColor} />
      </TouchableOpacity>

      <TouchableOpacity onPress={showAlert} style={styles.customButton}>
        <Text style={styles.buttonText}>Clique aqui</Text>
      </TouchableOpacity>

    </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  box: {
    borderWidth: 2,          
    borderColor: '#4CAF50', 
    borderRadius: 10,        
    padding: 80,             
    alignItems: 'center',
  },

  image: {
    width: 100,
    height: 100,
    marginBottom: 20, 
  },
  customButton: {
    backgroundColor: "green",
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 8,
    marginTop: 20, 
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
  input: {
    width: '100%', 
    height: 40,
    borderWidth: 1,
    borderRadius: 5,
    marginBottom: 20, 
    paddingHorizontal: 10,
  }
});
