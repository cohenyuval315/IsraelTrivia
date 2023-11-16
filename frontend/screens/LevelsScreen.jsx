// MainScreen.jsx
import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView, TouchableOpacity, Modal, Button } from 'react-native';
import LinearGradient from "react-native-linear-gradient";

const user_current_level_index = 3
const initial_levels = [
    {
        "level_id": 0,
        "index": 1,
        "level_name": "Level"
    },
    {
        "level_id": 1,
        "index": 2,
        "level_name": "Level"
    },
    {
        "level_id": 2,
        "index": 3,
        "level_name": "Level"
    },
]

const levels = initial_levels.map((item) => {
    item['locked'] = user_current_level_index > item.index ? false : true;
    return item;
});

const LevelScreen = ({ navigation }) => {
    const [modalVisible, setModalVisible] = useState(false);
    const [selectedLevel, setSelectedLevel] = useState(null);

    const handleLevelPress = (level) => {
        if (!level.locked) {
            setSelectedLevel(level);
            setModalVisible(true);
        } else {
            console.log(`Level ${level.level_name} is locked!`);
        }
    };

    const navigateToGame = () => {
        setModalVisible(false);
        // Update the navigation to pass necessary parameters
        navigation.navigate('Trivia', { selectedLevel });
    }

    return (

            <View >
                {/* Header with Logout Button */}
                <View style={{ padding: 10, backgroundColor: 'lightblue' }}>
                    <Button title="Logout" onPress={() => null} />
                </View>

                {/* Scroll View with Level Blocks */}
                <ScrollView contentContainerStyle={{ padding: 10, alignItems: 'center' }}>
                    {levels.map((level, index) => (
                        <View key={level.level_id} style={{justifyContent: 'flex-end', alignItems: 'center' }}>
                            <TouchableOpacity
                                onPress={() => handleLevelPress(level)}
                                style={{
                                    width: 50,
                                    height: 50,
                                    justifyContent: 'center',
                                    alignItems: 'center',
                                    marginVertical: 5,
                                    marginRight: 5,
                                    backgroundColor: level.locked ? 'lightblue' : 'gray',
                                    borderRadius: 25,
                                    overflow: 'hidden',
                                    borderColor: 'black',  // Add this line to add a black border
                                    borderWidth: 2,       // Add this line to set the border width
                                }}
                            >

                                <View style={{ alignItems: 'center' }}>
                                    <Text>{level.level_name}</Text>
                                    <Text>{level.level_id}</Text>
                                </View>
                            </TouchableOpacity>

                        </View>
                    ))}

                </ScrollView>

                {/* Modal for Level Data */}
                <Modal
                    animationType="slide"
                    transparent={false}
                    visible={modalVisible}
                    onRequestClose={() => setModalVisible(false)}
                >
                    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
                        <View style={{ padding: 20, backgroundColor: 'white', borderRadius: 10 }}>
                            {selectedLevel && selectedLevel.index === user_current_level_index ? (
                                <>
                                    <Text>Level Details</Text>
                                    <Text>Name: {selectedLevel?.level_name}</Text>
                                    <Button title={"Start"} onPress={navigateToGame}></Button>
                                </>
                            ) : (
                                <>
                                    <Text>Level Details</Text>
                                    <Text>Name: {selectedLevel?.level_name}</Text>
                                    {/* Add other properties if needed */}
                                    <Button title={"Play Again"} onPress={navigateToGame}></Button>
                                </>
                            )}
                            <Button title="Close" onPress={() => setModalVisible(false)} />
                        </View>
                    </View>
                </Modal>
            </View>

    );
};

export default LevelScreen;
