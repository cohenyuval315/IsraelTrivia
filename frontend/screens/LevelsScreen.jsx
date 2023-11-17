// MainScreen.jsx
import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView, TouchableOpacity, Modal, Button,StyleSheet } from 'react-native';
import api_client from '../services/ApiClient';
import LevelIconComponent from '../components/LevelIconComponent';
import {LinearGradient} from 'expo-linear-gradient';
import LevelDetails from '../components/LevelDetails';
import { useFocusEffect } from '@react-navigation/native';
import LevelSeparator from '../components/LevelSeparator';
import LevelsHeader from '../components/LevelsHeader';




const LevelScreen = ({ navigation }) => {
    const [modalVisible, setModalVisible] = useState(false);
    const [selectedLevel, setSelectedLevel] = useState(null);
    const [currentLevelIndex,setCurrentLevelIndex] = useState(null)
    const [levelsData,setLevelData] = useState(null)

    const [levels,setLevels] = useState(null)
    const [isLoading,setIsLoading] = useState(true)

    const fetchData = () => {
        console.log("init");
        api_client.getAppData().then((data)=>{
            app_levels = [...data['data']['levels']]
            setLevelData(app_levels);
            api_client.getUserProfile().then((user_data)=>{
                
                const unlocked_levels = user_data['levels_highscores']
                const current_level_index = user_data['current_level_index']
                setCurrentLevelIndex(current_level_index)
                const locked_levels = app_levels.filter((level)=> level.level_index > current_level_index)
                setLevels([...unlocked_levels.map((item)=>{item['unlocked']=true; return item}),...locked_levels.map((item)=>{item['unlocked']=false;return item;})].reverse())


            }).catch((user_error)=>console.log(user_error))

            setIsLoading(false)
        }).catch((error)=>
        console.log(error))
    }

    useFocusEffect(
        React.useCallback(() => {
          // This function will be called when the screen gains focus
    
          // Add the logic you want to execute when the screen is focused
          fetchData();
    
          // You can add more logic here if needed
    
          return () => {
            // This function will be called when the screen loses focus
            // You can clean up any resources or subscriptions here if needed
          };
        }, [/* dependencies that should trigger the effect */])
    );

    useEffect(()=>{
        fetchData()

    },[])

    const handleLevelPress = (level) => {
        if (level.unlocked) {
            setSelectedLevel(level);
            setModalVisible(true);
            console.log(level)
        } else {
            console.log(`Level ${level.level_name} is locked!`);
        }
    };

    const navigateToGame = () => {
        setModalVisible(false);
        // Update the navigation to pass necessary parameters
        const selectedLevelData = getSelectedLevelData()
        navigation.navigate('Trivia', { selectedLevel ,selectedLevelData  });
    }
    const onLogoutPress = () => {


    }

    const getSelectedLevelData = () => {
        if (selectedLevel && levelsData){
            return levelsData.filter((item)=>item['level_id'] === selectedLevel['level_id'])[0]
        }
        return {}
    }

    return (
        <>
            {!isLoading && (
                <LinearGradient colors={['#6DE5B5', '#0039C0']} start={{ x: 1.2, y: 0 }} end={{ x: 0 , y: 1 }} style={styles.container}>
            <View style={{flex:1}}>
                {/* Header with Logout Button */}
                <LevelsHeader userName={"Test"} currentLevel={currentLevelIndex} onLogoutPress={onLogoutPress}/>

                {/* Scroll View with Level Blocks */}
                <ScrollView
                      showsVerticalScrollIndicator={false}
                      showsHorizontalScrollIndicator={false}
                >
                    {levels && levels.map((level, index) => (
                    <React.Fragment key={`level_${index}`}>
                        {level.level_index === levels.length - 1 ? (
                        <>
                            {/* Render content for the last level */}
                        </>
                        ) : (
                        <>
                            {level.level_index > currentLevelIndex - 1 ? (
                            <LevelSeparator key={`level_separator_${index}`} colored={false} />
                            ) : (
                            <LevelSeparator key={`level_separator_${index}`} colored={true} />
                            )}
                        </>
                        )}
                        <LevelIconComponent key={`level_icon_${index}`} level={level} onPress={handleLevelPress} />
                    </React.Fragment>
                    ))}

                </ScrollView>

                {/* Modal for Level Data */}
                <Modal
                    animationType="slide"
                    transparent={false}
                    visible={modalVisible}
                    onRequestClose={() => setModalVisible(false)}>
                        <LevelDetails lastest={selectedLevel && selectedLevel.level_index === currentLevelIndex} level={selectedLevel} levelData={getSelectedLevelData()} onStart={navigateToGame} onClose={() => setModalVisible(false)} />
                    

                </Modal>
            </View>
            </LinearGradient>
            )}
        </>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'linearGradient(0,0,0,0)', // Set your desired background color
        paddingLeft: 15,
        paddingRight: 15,
        borderRadius: 5
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
        backgroundColor: '#3498db', // Default button color
        paddingVertical: 10,
        paddingHorizontal: 20,
        borderRadius: 5,
        marginBottom: 10,
    },
    buttonText: {
        color: '#fff', // Button text color
        fontSize: 18,
        textAlign: 'center',
    },
    linearGradient: {

    }
});

export default LevelScreen;
