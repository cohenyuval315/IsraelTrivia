// LevelDetailsModal.js
import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import Modal from 'react-native-modal';

const LevelDetailsModal = ({ isVisible, levelNumber, closeModal }) => (
    <Modal
        isVisible={isVisible}
        onBackdropPress={closeModal}
        style={{ justifyContent: 'flex-end', margin: 10 }}
    >
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <View style={{ backgroundColor: 'white', borderRadius: 10, padding: 16, width: '80%' }}>
                <Text>Level {levelNumber} Details</Text>
                <TouchableOpacity onPress={closeModal}>
                    <Text>Close</Text>
                </TouchableOpacity>
            </View>
        </View>
    </Modal>
);

export default LevelDetailsModal;
