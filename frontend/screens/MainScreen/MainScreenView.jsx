// MainScreenStyles.js
import { StyleSheet } from 'react-native';

const MainScreenView = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    footer: {
        padding: 10,
    },
    footerText: {
        textAlign: 'center',
        fontSize: 16,
        fontFamily: 'Inter', // Specify the font family here
    },
});

export default MainScreenView;
