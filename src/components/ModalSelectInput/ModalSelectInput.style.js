import { StyleSheet } from 'react-native'

export default StyleSheet.create({
    textValue:{
        color: '#333333',
        fontWeight: '400',
        fontSize: 14,
    },
    modalContainer: {
        flex: 1,
        justifyContent: 'center',
    },
    modalContent: {
        alignSelf: 'center',
        width: 301,
        height: 397,
        backgroundColor: '#fff',
        borderRadius: 8
    },
    header: {
        marginVertical: 20,
        marginHorizontal: 35,
        flexDirection: 'row',
        justifyContent: 'space-between'
    },
    title: {
        color: '#333333',
        fontWeight: '700',
        fontSize: 18,
        lineHeight: 20.7
    }
})
