import React, {useState} from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
} from 'react-native';
import {useLocation} from '../hooks/useLocation';
import {reportEmergency} from '../services/api';

export default function EmergencyReportScreen() {
  const [description, setDescription] = useState('');
  const [emergencyType, setEmergencyType] = useState('medical');
  const {location, getLocation} = useLocation();
  const [loading, setLoading] = useState(false);

  const handleReport = async () => {
    if (!description.trim()) {
      Alert.alert('Error', 'Please provide a description');
      return;
    }

    try {
      setLoading(true);
      await getLocation();

      const emergencyData = {
        emergency_type: emergencyType,
        description: description,
        location: {
          lat: location?.latitude,
          lng: location?.longitude,
        },
        location_lat: location?.latitude,
        location_lng: location?.longitude,
      };

      const response = await reportEmergency(emergencyData);
      Alert.alert('Success', 'Emergency reported successfully');
      setDescription('');
    } catch (error: any) {
      Alert.alert('Error', error.message || 'Failed to report emergency');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Report Emergency</Text>

      <TextInput
        style={styles.input}
        placeholder="Describe the emergency"
        multiline
        numberOfLines={4}
        value={description}
        onChangeText={setDescription}
      />

      <TouchableOpacity
        style={[styles.button, loading && styles.buttonDisabled]}
        onPress={handleReport}
        disabled={loading}>
        <Text style={styles.buttonText}>
          {loading ? 'Reporting...' : 'Report Emergency'}
        </Text>
      </TouchableOpacity>

      {location && (
        <Text style={styles.locationText}>
          Location: {location.latitude.toFixed(4)}, {location.longitude.toFixed(4)}
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 12,
    marginBottom: 20,
    minHeight: 100,
    textAlignVertical: 'top',
  },
  button: {
    backgroundColor: '#0ea5e9',
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  locationText: {
    marginTop: 10,
    fontSize: 12,
    color: '#666',
  },
});

