import React, { useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import GestureRecognizer, { swipeDirections } from 'react-native-swipe-gestures';

const StatementScreen = ({ statement, onWrongAnswer,onCorrectAnswer }) => {
    const [showSolution, setShowSolution] = useState(false);
    const right = 1;
    const left = 0;
    const handleSwipe = (gestureName) => {
        if (gestureName === 'SWIPE_RIGHT'){

        }else{

        }
        const isCorrect = statement.right_answer_index === 0;
        if (isCorrect === true){
            onCorrectAnswer();
        }else{
            onWrongAnswer();
        }
    };

    const config = {
        velocityThreshold: 0.3,
        directionalOffsetThreshold: 80,
    };

    return (
        <GestureRecognizer
            onSwipe={(direction, state) => handleSwipe(direction)}
            config={config}
            style={styles.container}
        >
            <View style={styles.card}>
                <Text style={styles.statementText}>{showSolution ? statement.solution : statement.statement[0].en}</Text>
                {showSolution && (
                    <View style={styles.references}>
                        <Text>References:</Text>
                        {statement.references.map((ref, index) => (
                            <Text key={index}>{ref}</Text>
                        ))}
                    </View>
                )}
            </View>
        </GestureRecognizer>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    card: {
        backgroundColor: 'white',
        padding: 20,
        borderRadius: 10,
        elevation: 5,
        shadowColor: 'black',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.3,
        shadowRadius: 3,
    },
    statementText: {
        fontSize: 18,
        marginBottom: 10,
    },
    references: {
        marginTop: 20,
    },
});

export default StatementScreen;
