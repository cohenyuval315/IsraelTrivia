// MainScreen.jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import LevelsScreen from "./LevelsScreen";

const MainScreen = () => {
    return (
        <LevelsScreen/>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default MainScreen;
