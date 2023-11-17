// FontLoader.js
import * as Font from 'expo-font';

export const loadSonsieOne = async () => {
    try {
        await Font.loadAsync({
            'SonsieOne': require('../assets/Fonts/SonsieOne-Regular.ttf'),
        });
    } catch (error) {
        console.error('Error loading font:', error);
    }
};

export const loadInter = async () => {
    try {
        await Font.loadAsync({
            'loadInter': require('../assets/Fonts/Inter-VariableFont_slnt,wght.ttf'),
        });
    } catch (error) {
        console.error('Error loading font:', error);
    }
};
