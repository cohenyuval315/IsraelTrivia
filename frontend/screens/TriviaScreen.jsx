import React, {useEffect, useState} from 'react';
import StatementScreen from "./StatementScreen";
import api_client from '../services/ApiClient';
import {LinearGradient} from 'expo-linear-gradient';
import StatementHeader from '../components/StatementHeader';
import FinishScreen from './FinishScreen';
import { useNavigation } from '@react-navigation/native';

const TriviaScreen = ({ route }) => {
    const { selectedLevel,selectedLevelData } = route.params;
    const [statements,setStatements] = useState(null)
    const [score, setScore] = useState(0);
    const [currentStatementIndex, setCurrentStatementIndex] = useState(0);
    
    const [loading,setLoading] = useState(true);
    const navigation = useNavigation();

    useEffect(()=>{
        api_client.getLevelStatements(selectedLevel.level_id).then((data)=>{
            setStatements(data);
            setLoading(false);
        }).catch((error)=>{
            console.log(error)
        })
    },[selectedLevel])


    const onCorrectAnswer = () => {
        
        const num_score_to_add = statements[currentStatementIndex].difficulty * 10
        setScore(prev=> prev + num_score_to_add);
        setCurrentStatementIndex(prev => prev + 1);
    }

    const onWrongAnswer = () => {
        setCurrentStatementIndex(prev => prev + 1);
    }

    const goToMainScreen = () => {
        navigation.navigate('Main');
      };


    const onClose = async () => {
        goToMainScreen();
        await api_client.updateUserProgress(selectedLevel['level_id'],selectedLevel['level_index'],score);
    }

    return (
        <>
        {!loading && (
            <>            
                {statements && statements.length > currentStatementIndex ? (<>
                <LinearGradient colors={['rgba(0, 0, 50, 0.9)', 'rgba(0, 0, 50, 0.7)']} style={{flex:1,flexGrow:1,flexDirection:"column"}}> 
                        <StatementHeader score={score} currentStatementIndex={currentStatementIndex} level={selectedLevel} levelData={selectedLevelData} onTimerExpired={onWrongAnswer}/>
                        <StatementScreen statement={statements[currentStatementIndex]} onCorrectAnswer={onCorrectAnswer} onWrongAnswer={onWrongAnswer} />
                </LinearGradient>
                </>) : (<>
                    <FinishScreen score={score} level={selectedLevel} levelData={selectedLevelData} onClose={onClose}/>            
                </>)}
            </>
        )}
        </>
    );
};



export default TriviaScreen;
