import React, { useState } from 'react'
import { Modal, Pressable, Text, TextInput, View, TouchableOpacity } from 'react-native';
import styles from './ModalSelectInput.style'

const ModalSelectInput = ({title}) => {
    const [modalVisible, setModalVisible] = useState(false);
    const [backgroundColor, setBackgroundColor] = useState('');
    return(
        <>
            <TouchableOpacity style={styles.container} onPress={()=>setModalVisible(true)}>
                <Text style={styles.textValue}>USA</Text>
            </TouchableOpacity>

            <Modal
                visible={modalVisible}
                transparent={true}
                animationType='slide'
                onShow={()=> setBackgroundColor('#33333380')}
            >
                <View style={[styles.modalContainer, {backgroundColor}]}>
                    <View style={styles.modalContent}>
                        <View style={styles.header}>
                            <View/>
                            <Text style={styles.title}>{title}</Text>
                            <Text onPress={()=>setModalVisible(false)}>X</Text>
                        </View>
                    </View>
                </View>
            </Modal>
        </>
    )
}

export default ModalSelectInput;