import React, {useEffect, useState} from 'react';
import {View, Text, StyleSheet, FlatList, RefreshControl} from 'react-native';
import {getMyCases} from '../services/api';

export default function CaseStatusScreen() {
  const [cases, setCases] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const loadCases = async () => {
    try {
      setLoading(true);
      const data = await getMyCases();
      setCases(data);
    } catch (error) {
      console.error('Error loading cases:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadCases();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>My Cases</Text>
      <FlatList
        data={cases}
        keyExtractor={item => item.case_id}
        refreshControl={
          <RefreshControl refreshing={loading} onRefresh={loadCases} />
        }
        renderItem={({item}) => (
          <View style={styles.caseItem}>
            <Text style={styles.caseId}>{item.case_id}</Text>
            <Text style={styles.status}>Status: {item.status}</Text>
            <Text style={styles.severity}>Severity: {item.severity_level}</Text>
          </View>
        )}
        ListEmptyComponent={
          <Text style={styles.emptyText}>No cases found</Text>
        }
      />
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
  caseItem: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  caseId: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  status: {
    marginTop: 4,
    color: '#666',
  },
  severity: {
    marginTop: 4,
    color: '#666',
  },
  emptyText: {
    textAlign: 'center',
    marginTop: 40,
    color: '#999',
  },
});

