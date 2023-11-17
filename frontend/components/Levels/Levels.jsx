// Levels.js
import React, { useRef, useEffect, useState } from 'react';
import { View, ScrollView } from 'react-native';
import Level from './Level';
import LevelDetailsModal from '../LevelDetailsModal';

const Levels = ({ userData }) => {
    const { currentLevel } = userData;
    const openLevels = Array.from({ length: currentLevel }, (_, i) => i + 1);
    const buttonCount = 20;
    const scrollViewRef = useRef(null);
    const modalRef = useRef(null);
    const [selectedLevel, setSelectedLevel] = useState(null);

    useEffect(() => {
        if (scrollViewRef.current) {
            scrollViewRef.current.scrollToEnd({ animated: false });
        }
    }, [scrollViewRef, buttonCount]);

    const handleLevelPress = (levelNumber) => {
        setSelectedLevel(levelNumber);
        modalRef.current?.open?.(); // Use optional chaining to check if modalRef.current and modalRef.current.open exist
    };

    const closeModal = () => {
        setSelectedLevel(null);
        modalRef.current?.close?.(); // Use optional chaining to check if modalRef.current and modalRef.current.close exist
    };

    return (
        <View style={{ flex: 0.9, justifyContent: 'flex-end', alignItems: 'center' }}>
            <ScrollView
                ref={scrollViewRef}
                contentContainerStyle={{ flexGrow: 1, justifyContent: 'flex-end', alignItems: 'center' }}
                style={{ flex: 0.9, width: '100%' }}
                onContentSizeChange={() => {
                    scrollViewRef.current.scrollToEnd({ animated: false });
                }}
            >
                {[...Array(buttonCount).reverse()].map((_, index) => (
                    <Level
                        key={index + 1}
                        levelNumber={buttonCount - index}
                        isOpen={openLevels.includes(buttonCount - index)}
                        onPress={handleLevelPress}
                    />
                ))}
            </ScrollView>

            <LevelDetailsModal
                ref={modalRef}
                isVisible={selectedLevel !== null}
                levelNumber={selectedLevel}
                closeModal={closeModal}
            />
        </View>
    );
};

export default Levels;
