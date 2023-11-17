// MainScreen.jsx
import React, {useEffect, useState} from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Levels from "../../components/Levels/Levels";
import { SafeAreaView } from 'react-native-safe-area-context';
import MainScreenView from './MainScreenView';
import LinearGradientBackground from "../../assets/Colors/BackgroundColorComponent";


const MainScreen = ({ navigation }) => {

    //MockData
    const userData = { ID: 'someId', currentLevel: 1, Life: 3 };

    return (
        <LinearGradientBackground>
            <SafeAreaView style={MainScreenView.container}>
                <Levels navigation={navigation} userData={userData} />
                <View style={MainScreenView.footer}>
                    <Text style={[MainScreenView.footerText]}>
                        Please click on the next level you want to play.
                        You can only open a level if you have already passed the previous one.
                    </Text>
                </View>
            </SafeAreaView>
        </LinearGradientBackground>
    );
};

export default MainScreen;
