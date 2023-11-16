// MainScreen.jsx
import React, {useEffect, useState} from 'react';
import {View, Text, StyleSheet, Modal} from 'react-native';
import LevelsScreen from "./LevelsScreen";
import StatementScreen from "./StatementScreen";


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

const get_statement = (index) => {
    const statement = {
        "statement_id": `${index}`,
        "statement": [
            {
                "en": "statement statement statement statement statement statement statement statement statement statement 1"
            }
        ],
        "difficulty": 1,
        "options": [
            {
                "en":"true"
            },
            {
                "en":"false"
            }
        ],
        "right_answer_index": 0,
        "solution": "this is the full description of the solution of this question.... blablabla from the history of today blabalba... for more reference you can read below blablabla...",
        "references": ["reflink.com","ref2link.com"]
    }
    return statement;
}

const get_level_statements = () => {
    const statements = [
        get_statement(0),
        get_statement(1),
        get_statement(2),
        get_statement(3),
        get_statement(4),
        get_statement(5),
        get_statement(6),
        get_statement(7),
        get_statement(8),
        get_statement(9),
    ]
    return statements;
}






const TriviaScreen = ({ route }) => {
    const { selectedLevel } = route.params;
    const level = get_level(selectedLevel.level_id);
    const statements = get_level_statements(level.level_id);
    const num_statements = level.num_questions;
    const [score, setScore] = useState(0);
    const [currentStatementIndex, setCurrentStatementIndex] = useState(0);

    const [modalVisible,setModalVisible] = useState(false);

    useEffect(()=>{
        if(currentStatementIndex + 1 > num_statements){
            onFinish();
        }
    },[currentStatementIndex])

    const onFinish = () => {
        setModalVisible(true);
        // update_user_progress function from db
    }

    const onCorrectAnswer = () => {
        setCurrentStatementIndex(prev => prev + 1);
        const num_score_to_add = statements[currentStatementIndex].difficulty * 10
        setScore(prev=> prev + num_score_to_add);
    }

    const onWrongAnswer = () => {
        setCurrentStatementIndex(prev => prev + 1);
        const num_score_to_add = statements[currentStatementIndex].difficulty * 10
    }


    return (
        <>
            {! currentStatementIndex + 1 > num_statements ? (<>
                <Modal
                    visible={modalVisible}
                    onRequestClose={() => setModalVisible(false)}

                >
                    <Text>{level.level_name}</Text>
                    {score > level.min_score ? (<>

                    </>) : (<>

                    </>)}
                </Modal>
            </>) : (<>
                    <Text>{level.level_name}</Text>
                    <Text>Current Score: {score}</Text>
                    <Text>{currentStatementIndex}/{num_statements}</Text>
                    <StatementScreen  statement={statements[currentStatementIndex]} onCorrectAnswer={onCorrectAnswer} onWrongAnswer={onWrongAnswer} />
            </>)}


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
