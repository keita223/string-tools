from string_tools.string_ops import reverse_string, count_vowels, capitalize_words


class TestStringOps:
    """Tests pour les fonctions de manipulation de strings."""

    def test_reverse_string(self):
        """Test de la fonction reverse_string."""
        # Test cas normal
        assert reverse_string("hello") == "olleh"
        assert reverse_string("python") == "nohtyp"

        # Test string vide
        assert reverse_string("") == ""

        # Test un seul caractère
        assert reverse_string("a") == "a"

    def test_count_vowels(self):
        """Test de la fonction count_vowels."""
        # Test cas normal
        assert count_vowels("hello") == 2  # e, o
        assert count_vowels("AEIOU") == 5  # toutes les voyelles majuscules

        # Test sans voyelles
        assert count_vowels("xyz") == 0

        # Test string vide
        assert count_vowels("") == 0

        # Test mixte majuscules/minuscules
        assert count_vowels("Hello World") == 3  # e, o, o

    def test_capitalize_words(self):
        """Test de la fonction capitalize_words."""
        # Test cas normal
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python programming") == "Python Programming"

        # Test déjà capitalisé
        assert capitalize_words("Hello World") == "Hello World"

        # Test un seul mot
        assert capitalize_words("hello") == "Hello"

        # Test string vide
        assert capitalize_words("") == ""
