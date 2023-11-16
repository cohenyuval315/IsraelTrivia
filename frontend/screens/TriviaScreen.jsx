// MainScreen.jsx
import React, {useState} from 'react';
import { View, Text, StyleSheet } from 'react-native';
import LevelsScreen from "./LevelsScreen";


const last_level_highscore = {
    "level_id":"1",
    "level_index": 2,
    "highscore": 200,
    "date": "10-10-2000"
}

const new_level_highscore = {
    "level_id":"1",
    "level_index": 2,
    "highscore": 0,
    "date": "10-10-2000"
}



const get_level = (level_id) => {
    const level = {
        "level_id":level_id,
        "index": 2,
        "level_name": "Intermediate-1",
        "num_questions": 10,
        "question_difficulty_distribution": [0, 50, 50, 0, 0],
        "min_score": 50
    }
    return level;
}



const StatementScreen = ({index,statement}) => {
    return (
        <>
        </>
    )
}
const statements = [
    {
        "statement":"question 2"

    }
]

const get_level_statements = ({statement,onFinish}) => {
    const onAnswer = () => {
        if
    }
}

const TriviaScreen = ({ route }) => {
    const { selectedLevel } = route.params;
    const level = get_level(selectedLevel.level_id);
    const statements = get_level_statements(level.level_id);
    const num_statements = level.num_questions;
    const [score, setScore] = useState(0);
    const [currentStatementIndex, setCurrentStatementIndex] = useState(0);


    const onFinish = () => {
        setCurrentStatementIndex(prev => prev + 1);
    }
    return (
        <>
            <Text>{level.level_name}</Text>
            <Text>Current Score: {score}</Text>
            <Text>{currentStatementIndex}/{num_statements}</Text>
            <StatementScreen  statement={statements[currentStatementIndex]} onFinish={onFinish} />
        </>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default TriviaScreen;
