import React from 'react'
import { Pressable, Text, TextInput, View } from 'react-native'
import ModalSelectInput from '../ModalSelectInput/ModalSelectInput.screen'
import styles from './SignUp.style'

const SignUp = ({}) => {
    return(
        <>
            <View style={styles.container}>
                <Text style={styles.title}>Welcome!</Text>
                <Text style={styles.description}>You are signing up with your account in</Text>
                <ModalSelectInput title='Select Country'/>
                <View style={styles.formContainer}>
                    <Text style={styles.formLabel}>Email</Text>
                    <TextInput style={styles.textForm} placeholder='Your email address' placeholderTextColor='#33333370'/>
                </View>
                <View style={styles.formContainer}>
                    <Text style={styles.formLabel}>Password</Text>
                    <TextInput style={styles.textForm} placeholder='Your password' placeholderTextColor='#33333370'/>
                </View>
                <View style={styles.formContainer}>
                    <Text style={styles.formLabel}>Confirm Password</Text>
                    <TextInput style={styles.textForm} placeholder='Confirm your password' placeholderTextColor='#33333370'/>
                </View>
                <Pressable style={styles.actionButton}>
                    <Text style={styles.actionText}>Sign-up</Text>
                </Pressable>
            </View>
        </>
    )
}

export default SignUp;