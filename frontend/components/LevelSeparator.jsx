
// MainScreen.jsx
import React from 'react';
import { View } from 'react-native';

const LevelSeparator = ({colored}) => {
    const backgroundColor = colored === false ? "black" : "blue" 
    return (
        <>
            <View style={{ alignItems: 'center', justifyContent: 'center' }}>
                    <View style={{ flexDirection: 'column', alignItems: 'center' }}>
                    <View style={{ width: 6, height: 6, backgroundColor: backgroundColor, borderRadius: 3, marginBottom: 2 }} />
                    <View style={{ width: 6, height: 6, backgroundColor: backgroundColor, borderRadius: 3, marginBottom: 2 }} />
                    <View style={{ width: 6, height: 6, backgroundColor: backgroundColor, borderRadius: 3 }} />
                    </View>
            </View>
        </>
    );
  };

export default LevelSeparator;