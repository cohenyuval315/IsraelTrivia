// LoginScreen.jsx
import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';
import LinearGradientBackground from "../../assets/Colors/BackgroundColorComponent";

const LoginScreen = ({ navigation }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = () => {
        // Perform login logic here
        // For simplicity, let's just navigate to the MainScreen
        navigation.navigate('Stack2');
    };

    return (
        <LinearGradientBackground>
            <View style={styles.container}>
                <Text style={{ color: '#fff' }}>Login</Text>
                <TextInput
                    placeholder="Username"
                    placeholderTextColor="#fff"  // Set placeholder text color
                    value={username}
                    onChangeText={setUsername}
                    style={styles.input}
                />
                <TextInput
                    placeholder="Password"
                    placeholderTextColor="#fff"  // Set placeholder text color
                    value={password}
                    onChangeText={setPassword}
                    secureTextEntry
                    style={styles.input}
                />
                <Button
                    title="Login"
                    onPress={handleLogin}
                    color="#fff"  // Set button text color
                    style={styles.loginButton}
                />
            </View>
        </LinearGradientBackground>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    input: {
        width: '80%',
        height: 40,
        borderColor: '#fff',
        borderWidth: 1,
        marginVertical: 10,
        padding: 8,
        color: '#fff',  // Set text color
    },
    loginButton: {
        marginTop: 20,
        backgroundColor: '#3498db',  // Set button background color
        padding: 10,
        borderRadius: 5,
    },

});

export default LoginScreen;
