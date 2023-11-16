// src/screens/MainPage.tsx
import * as React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const MainPage: React.FC = () => {
    return (
        <View style={styles.container}>
            <Text>Main Screen</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default MainPage;
