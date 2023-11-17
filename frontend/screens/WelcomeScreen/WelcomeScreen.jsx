// WelcomeScreen.js
import React, { useEffect, useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { loadSonsieOne } from '../../components/FontLoader';
import useFontLoader from "../../components/customHooks/useFontLoader";


const WelcomeScreen = ({ navigation }) => {

    const fontLoaded = useFontLoader(loadSonsieOne);

    if (!fontLoaded) {
        return null; // You can also render a loading indicator here
    }


    return (
        <LinearGradient colors={['#6DE5B5', '#0039C0']} start={{ x: 1.2, y: 0 }} end={{ x: 0 , y: 1 }} style={styles.container}>
            <View>
                <Text style={[styles.swipeText, { fontFamily: 'SonsieOne' }]}>Swipe</Text>
                <Text style={[styles.masterText, { fontFamily: 'SonsieOne' }]}>Master</Text>
                <TouchableOpacity
                    style={styles.button}
                    onPress={() => navigation.navigate('Login')}
                >
                    <Text style={styles.buttonText}>Login</Text>
                </TouchableOpacity>

                <TouchableOpacity
                    style={[styles.button, { backgroundColor: '#27ae60' }]}
                    onPress={() => navigation.navigate('Register')}
                >
                    <Text style={styles.buttonText}>Register</Text>
                </TouchableOpacity>
            </View>
        </LinearGradient>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        paddingLeft: 15,
        paddingRight: 15,
        borderRadius: 5,
    },
    swipeText: {
        color: 'white',
        fontSize: 50,
        fontWeight: '400',
        marginBottom: 10,
    },
    masterText: {
        color: 'white',
        fontSize: 50,
        fontWeight: '400',
        marginBottom: 20,
    },
    button: {
        backgroundColor: '#3498db',
        paddingVertical: 10,
        paddingHorizontal: 20,
        borderRadius: 5,
        marginBottom: 10,
    },
    buttonText: {
        color: '#fff',
        fontSize: 18,
        textAlign: 'center',
    },
});

export default WelcomeScreen;
