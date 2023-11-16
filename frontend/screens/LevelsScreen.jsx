// MainScreen.jsx

const user_current_level_index = 3
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
const levels = initial_levels.map((item)=>{
    if (user_current_level_index > item.index){
        item['locked'] = false;
    }else{
        item['locked'] = true;
    }
    return item

})
import React, {useEffect, useState} from 'react';
import { View, Text, ScrollView, TouchableOpacity, Modal, Button } from 'react-native';

const LevelScreen = ({navigation}) => {
    const [modalVisible, setModalVisible] = useState(false);
    const [selectedLevel, setSelectedLevel] = useState(null);


    useEffect(()=>{

    },[])


    const handleLevelPress = (level) => {
        if (!level.locked) {
            setSelectedLevel(level);
            setModalVisible(true);
        } else {
            // Handle locked level, e.g., show a message
            console.log(`Level ${level.level_name} is locked!`);
        }
    };

    const navigateToGame = () => {
        setModalVisible(false);
        navigation.navigate('Trivia', { selectedLevel });
    }
    return (
        <View style={{ flex: 1 }}>
            {/* Header with Logout Button */}
            <View style={{ padding: 10, backgroundColor: 'lightblue' }}>
                {/* Your header content, e.g., title, user info, etc. */}
                <Button title="Logout" onPress={null} />
            </View>

            {/* Scroll View with Level Blocks */}
            <ScrollView contentContainerStyle={{ padding: 10 }}>
                {levels.map((level, index) => (
                    <View key={level.level_id} style={{ flexDirection: 'row', alignItems: 'center' }}>
                        <TouchableOpacity
                            onPress={() => handleLevelPress(level)}
                            style={{
                                flex: 1,
                                padding: 10,
                                marginVertical: 5,
                                marginRight: 5,
                                backgroundColor: level.locked ? 'lightgray' : 'lightgreen',
                                alignItems: 'center',
                            }}
                        >
                            <Text>{level.level_name}</Text>
                            <Text>{level.locked ? 'Locked' : 'Unlocked'}</Text>
                        </TouchableOpacity>
                        {index < levels.length - 1 && (
                            <View style={{ width: 1, height: '100%', backgroundColor: 'gray' }} />
                        )}
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
                        {selectedLevel && selectedLevel.index === user_current_level_index?(
                            <>
                                <Text>Level Details</Text>
                                <Text>Name: {selectedLevel?.level_name}</Text>
                                <Button title={"start"} onPress={navigateToGame}></Button>
                            </>
                        ):(
                            <>
                                <Text>Level Details</Text>
                                <Text>Name: {selectedLevel?.level_name}</Text>
                                <Text>High score: {selectedLevel?.highscore}</Text>
                                <Button title={"play again"} onPress={navigateToGame}></Button>
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
