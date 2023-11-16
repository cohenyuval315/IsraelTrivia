// src/screens/WelcomeScreen.tsx
import * as React from 'react';

import { View, Text, Button, StyleSheet } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';

type WelcomeScreenProps = {
    navigation: StackNavigationProp<any, 'Welcome'>; // Replace 'any' with your stack params
};

const WelcomeScreen: React.FC<WelcomeScreenProps> = ({ navigation }) => {
    const handleLoginPress = () => {
        // Navigate to the login screen
        navigation.navigate('Login');
    };

    const handleRegisterPress = () => {
        // Navigate to the register screen
        navigation.navigate('Register');
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Welcome!</Text>
            <View style={styles.buttonContainer}>
                <Button title="Login"    onPress={handleLoginPress} />
                <Button title="Register" onPress={handleRegisterPress} />
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    title: {
        fontSize: 24,
        marginBottom: 16,
    },
    buttonContainer: {
        flexDirection: 'row',
        justifyContent: 'space-around',
        width: '60%',
    },
});

export default WelcomeScreen;
