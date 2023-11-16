// MainScreen.jsx
import React, {useState} from 'react';
import { View, Text, StyleSheet } from 'react-native';

const LevelsScreen = () => {
    const user_current_level_index = 2
    const initial_levels = [
        {
            "level_id":0,
            "index":1,
            "level_name":"hello"
        },
        {
            "level_id":1,
            "index":2,
            "level_name":"hello2"
        },
        {
            "level_id":2,
            "index":3,
            "level_name":"hello3"
        },
    ]
    const [levels , setLevels] = useState(initial_levels)

    return (
        <View style={styles.container}>

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

export default LevelsScreen;
