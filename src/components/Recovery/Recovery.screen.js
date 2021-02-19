import React from 'react'
import { Pressable, Text, TextInput, View } from 'react-native'
import styles from './Recovery.style'

const Recovery = ({}) => {
    return(
        <>
            <View style={styles.container}>
                <Text style={styles.title}>Password Recovery</Text>
                <Text style={styles.description}>If you forgot your password, please fill in the details below:</Text>
                <View style={styles.formContainer}>
                    <Text style={styles.formLabel}>Email</Text>
                    <TextInput style={styles.textForm} placeholder='Your email address' placeholderTextColor='#33333370'/>
                </View>
                <Pressable style={styles.actionButton}>
                    <Text style={styles.actionText}>Recovery</Text>
                </Pressable>
            </View>
        </>
    )
}

export default Recovery;