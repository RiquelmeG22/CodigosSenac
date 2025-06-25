import React, { useState } from 'react';
import AntDesign from '@expo/vector-icons/AntDesign';
import { Text, View, StyleSheet, Image, TouchableOpacity, TextInput, KeyboardAvoidingView, Platform } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import NewWindow from './NewWindow';


const Stack = createStackNavigator();


 function MainScreen({ navigation }) {
  const [heartColor, setHeartColor] = useState('green');
  const [backgroundColor, setBackgroundColor] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [secure, setSecure] = useState(true);
  const [loggedIn, setLoggedIn] = useState(false);

  const showAlert = () => {
    if (!username.trim() || !password.trim()) {
      alert('Preencha todos os campos antes de continuar.');
      return;
    }
  
    if (username === 'admin' && password === 'admin') {
      setLoggedIn(true);
      alert(`Login efetuado com sucesso!`);
      navigation.navigate('NewWindow');
    } else {
      alert('Usuário ou senha inválido.');
      setLoggedIn(false);
    }
  };
  

  return (
    <View style={[styles.container, { backgroundColor }]}>
      {/* Renderiza a imagem somente se logado */}
      {loggedIn && (
        <Image
          source={{ uri: 'https://github.com/RiquelmeG22.png' }}
          style={styles.image}
        />
      )}

      <Text style={styles.text}>LOGIN</Text>

      <TextInput
        style={styles.input}
        placeholder="Username"
        onChangeText={text => setUsername(text)}
        value={username}
      />

      <View style={styles.passwordContainer}>
        <TextInput
          style={styles.inputPassword}
          placeholder="Senha"
          secureTextEntry={secure}
          onChangeText={text => setPassword(text)}
          value={password}
        />
        <TouchableOpacity onPress={() => setSecure(!secure)}>
          <AntDesign name={secure ? 'eyeo' : 'eye'} size={24} color="gray" />
        </TouchableOpacity>
      </View>

      <TouchableOpacity onPress={showAlert} style={styles.customButton}>
        <Text style={styles.buttonText}>Clique aqui</Text>
      </TouchableOpacity>
    </View>
  );
}

export default function App() {

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName = "Main">
        <Stack.Screen name="Main" component={MainScreen} options={{ title: 'Tela Principal'}}/>
        <Stack.Screen name="NewWindow" component={NewWindow} options={{ title: 'NewWindow'}}/>

      </Stack.Navigator>
    </NavigationContainer>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  image: {
    width: 150,
    height: 150,
    borderRadius: 100,
    marginBottom: 20,
  },
  text: {
    fontSize: 30,
    marginVertical: 10,
  },
  input: {
    width: '40%',
    height: 40,
    borderWidth: 1,
    borderRadius: 5,
    marginVertical: 10,
    paddingHorizontal: 10,
    backgroundColor: '#fff'
  },
  passwordContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '40%',
    borderWidth: 1,
    borderRadius: 5,
    backgroundColor: '#fff',
    paddingHorizontal: 10,
    marginVertical: 10,
  },
  inputPassword: {
    flex: 1,
    height: 40,
  },
  customButton: {
    marginTop: 20,
    padding: 10,
    backgroundColor: '#1E90FF',
    borderRadius: 5,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  }
});

